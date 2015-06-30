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
        self.conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=table)
        self.result = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def get_first_author(self):
        """
        get first author list
        """
        self.result.execute("SELECT author FROM listauthor order by author")

        author_list = []
        for each in self.result:
            a = str(each[0]).split(',')
            author_list.append( a[0] )

        with open("author_list.txt", 'w') as wfile:
            for each in author_list:
                wfile.writelines(each + "\n")

    def get_paper_list(self):
        """
        get plain paper list and field category
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
        self.result.execute("SELECT * FROM list order by year DESC")

        index = 1
        with open("paper_list.txt", 'w') as wf:
            for r in self.result:
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
                elif ( str(r[2]) == "inproceedings" ):
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

        self.result.close()

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


if __name__=='__main__':
    l = librarian()
    l.get_paper_list()




