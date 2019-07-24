# encoding:utf8
import csv
import conf


def make_qa_script_partial():
    qa_list = []
    qa_script = []

    with open(conf.WORKING_DIR + conf.QA_TEMPLATE) as f:
        template = f.read()

    with open(conf.WORKING_DIR + conf.QA_DATA) as f:
        csv_reader = csv.DictReader(f)
        line_count = 0
        for row in csv_reader:
            line_count += 1
            print(row)
            qa_item = {
                'A': row['A'],
                'B': row['B'],
                'C': row['C'],
                'D': row['D'],
                '题目': row['题目'],
                '正确答案': row[row['正确答案']],
                '正确选项': row['正确答案'].lower()+", "+row[row['正确答案']]
            }
            wrong_choices = []

            def append_wrong_choice(choice):
                if row['正确答案'] != choice:
                    wrong_choices.append(choice.lower())
                    wrong_choices.append(qa_item[choice])

            append_wrong_choice('A')
            append_wrong_choice('B')
            append_wrong_choice('C')
            append_wrong_choice('D')
            qa_item['错误选项'] = ", ".join(wrong_choices)
            qa_list.append(qa_item)
            print(qa_item)
        print(f'\n\nProcessed {line_count} qa items.')

    def template_replace(qa_item, template, index):
        template_copy = str(template)
        # 垃圾名称、错误选项、正确选项、正确答案
        template_copy = template_copy.replace('{序号}', str(index))
        template_copy = template_copy.replace('{n}', str(len(qa_list)))
        template_copy = template_copy.replace('{A}', qa_item['A'])
        template_copy = template_copy.replace('{B}', qa_item['B'])
        template_copy = template_copy.replace('{C}', qa_item['C'])
        template_copy = template_copy.replace('{D}', qa_item['D'])
        template_copy = template_copy.replace('{题目}', qa_item['题目'])
        template_copy = template_copy.replace('{正确答案}', qa_item['正确答案'])
        template_copy = template_copy.replace('{正确选项}', qa_item['正确选项'])
        template_copy = template_copy.replace('{错误选项}', qa_item['错误选项'])
        return template_copy

    for index, qa_item in enumerate(qa_list):
        qa_script.append(template_replace(qa_item, template, index+1))

    return len(qa_list), "\n".join(qa_script)


def generate_final_script(n, s):
    with open(conf.WORKING_DIR + conf.SCRIPT_TEMPLATE) as f:
        template = f.read()

    template_copy = str(template)
    template_copy = template_copy.replace("{n}", str(n))
    template_copy = template_copy.replace("{quiz}", s)

    with open(conf.WORKING_DIR + conf.SCRIPT_OUTPUT, 'w') as f:
        f.write(template_copy+"\n")


if __name__ == "__main__":
    n, s = make_qa_script_partial()
    generate_final_script(n, s)
    print("生成完毕")
