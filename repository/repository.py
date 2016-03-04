import json
import pymysql

class librarian:
    def __init__(self):
        d = json.load(fp=open("db.json"))
        host = d["db"][0]["host"]
        user = d["db"][0]["user"]
        table = d["db"][0]["table"]
        passwd = d["db"][0]["passwd"]
        # connect
        self.connection = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=table)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_first_author(self):
        """
        Return the list of all first authors.
        """
        self.cursor.execute('SELECT author FROM listauthor order by author')

        author_list = []
        for each in self.cursor:
            a = str(each[0]).split(',')
            author_list.append( a[0] )

        with open("author_list.txt", 'w') as wfile:
            for each in author_list:
                wfile.writelines(each + "\n")

    def get_paper_list(self):
        """
        Return plain citations of all paper
        """
        generation = ""
        application = ""
        model = ""
        evaluation = ""
        constraint = ""
        prioritization = ""
        diagnosis = ""
        survey = ""
        oracle = ""
        self.cursor.execute("SELECT * FROM list order by year DESC")

        index = 1
        with open("paper_list.txt", 'w') as wf:
            for r in self.cursor:
                # [index] + author + title  + "in" + publication
                content = "[" + str(index) + "] " + str(r[4]) + ", " + str(r[5]) + ", in " + str(r[6])

                # abbr
                abbr = str(r[7])
                if ( abbr not in ["None", "book", "phd", "tech"] ):
                    content += " (" + abbr + ")"

                # "vol(no): page, year" for article
                if ( str(r[2]) == "article" ):
                    content += ", " + str(r[8]) + "(" + str(r[9]) + "): " + str(r[10]) + ", " + str(r[3])
                # "year: page" for inproceedings
                elif ( str(r[2]) == "inproceedings" or str(r[2]) == "incollections" ):
                    content += ", " + str(r[3]) + ": " + str(r[10])
                # "TechNo, year" for techreport
                elif ( str(r[2]) == "techreport" ):
                    content += ", " + str(r[9]) + ", " + str(r[3])
                # for phdthesis and book
                else:
                    content += ", " + str(r[3])

                # 将unicode编码转换成其他编码的字符串
                con = content.encode('utf-8')
                # decode的作用是将其他编码的字符串转换成unicode编码，
                wf.writelines(con.decode('gbk') + "\n")

                # deal with the field
                if ( str(r[11]) == "Generation" ):
                    generation += "[" + str(index) + "], "
                elif ( str(r[11]) == "Application" ):
                    application += "[" + str(index) + "], "
                elif ( str(r[11]) == "Model" ):
                    model += "[" + str(index) + "], "
                elif ( str(r[11]) == "Evaluation" ):
                    evaluation += "[" + str(index) + "], "
                elif ( str(r[11]) == "Constraint" ):
                    constraint += "[" + str(index) + "], "
                elif ( str(r[11]) == "Prioritization" ):
                    prioritization += "[" + str(index) + "], "
                elif ( str(r[11]) == "Diagnosis" ):
                    diagnosis += "[" + str(index) + "], "
                elif ( str(r[11]) == "Survey" ):
                    survey += "[" + str(index) + "], "
                elif ( str(r[11]) == "Oracle" ):
                    oracle += "[" + str(index) + "], "

                index += 1

        self.cursor.close()

        # write field file
        with open("field.txt", 'w') as wf:
            generation = generation.encode('UTF-8')
            wf.writelines("generation: " + generation.decode('gbk') + "\n")

            application = application.encode('UTF-8')
            wf.writelines("application: " + application.decode('gbk') + "\n")

            model = model.encode('UTF-8')
            wf.writelines("model: " + model.decode('gbk') + "\n")

            evaluation = evaluation.encode('UTF-8')
            wf.writelines("evaluation: " + evaluation.decode('gbk') + "\n")

            constraint = constraint.encode('UTF-8')
            wf.writelines("constraint: " + constraint.decode('gbk') + "\n")

            prioritization = prioritization.encode('UTF-8')
            wf.writelines("prioritization: " + prioritization.decode('gbk') + "\n")

            diagnosis = diagnosis.encode('UTF-8')
            wf.writelines("diagnosis: " + diagnosis.decode('gbk') + "\n")

            survey = survey.encode('UTF-8')
            wf.writelines("survey: " + survey.decode('gbk') + "\n")

            oracle = oracle.encode('UTF-8')
            wf.writelines("oracle: " + oracle.decode('gbk') + "\n")


    def check_new_authors(self):
        """
        Check whether every author is in the scholar table. All new
        authors will be printed to console.
        """
        author_list = []    # all authors from scholar table
        result1 = self.connection.cursor()
        result1.execute('select name from scholar order by name')
        for each in result1:
            a = str(each[0])
            author_list.append(a)

        # get every author from paper table, and check their existences
        result2 = self.connection.cursor()
        result2.execute("select author from list")
        for each in result2:
            a = str(each[0]).split(',')
            for each_name in a:
                each_name = each_name.strip()
                if each_name not in author_list:
                    author_list.append(each_name)
                    print(each_name)


    def check_paper_json(self, filename):
        """
        Check whether every paper in filename.json is included in our database.
        The input json file is from DBLP database. All new papers will be written
        to a file.
        """
        p = json.load(fp=open(filename))
        papers = p['result']['hits']['hit']
        num = int(p['result']['hits']['@total'])

        new_title_list = []
        for i in range(0, num):
            each = papers[i]['info']['title']
            each = each[:len(each)-1]    # remove the dot in the end of title

            # check repository, perfect match
            self.cursor.execute('select id, title from list where title = "' + each + '"')
            result = self.cursor.fetchone()
            if (result is None):
                new_title_list.append(each)

        # write result to file
        with open("new_title_list.txt", 'w') as fw:
            for each in new_title_list:
                fw.write(each + '\n')


    def get_country_code_table(self, filename):
        p = json.load(fp=open(filename))
        country = []
        code = []

        for each in p:
            country.append(each['name'])
            code.append(each['code'])

        # write result to file
        with open("country code.txt", 'w') as fw:
            for i in range(0, len(country)):
                fw.write(country[i] + '|' + code[i] + '\n')


    def get_all_title(self):
        title = ''
        result1 = self.connection.cursor()
        result1.execute('select title from list')

        for each in result1:
            a = str(each[0])
            print(a)


