import pandas
import joblib
from sklearn.linear_model import LogisticRegression

def tomldata(mbti, sex, age, job, like):
    col_list = ['like',
                '남자', '여자',
                '10대', '20대', '30대', '40대', '50대', '60대 이상',
                '대학생', '무직', '미성년자', '사업가', '전업주부', '직장인', '프리랜서',
                'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ',
                'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP',
                'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

    ml_df = pandas.DataFrame(columns=col_list)

    list1 = []
    new = [mbti, sex, age, job]
    for i in range(4):
        list1.append(col_list.index(new[i]))

    list1.sort()

    list2 = [0 for i in range(32)]
    list2[0] = int(like)
    for i in range(4):
        list2[list1[i]] = 1

    ml_df.loc[0] = list2

    # 여기 절대경로!!!!!!!!!!!
    load_model = joblib.load('/Users/gim-yongbeom/PycharmProjects/Django/mbti_project/projectdo/mainPage/module/lr_clf.pkl')

    predict = load_model.predict([ml_df.loc[0]])
    # predict[0]
    # ml_df.loc[0]
    return predict[0]

# def load_data(input):
#     load_model = joblib.load('lr_clf.pkl')
#
#     predict = load_model.predict()
#
#     return load_model

# print(tomldata('ENFJ','남자','20대','무직',1))

#
# load_model = joblib.load('lr_clf.pkl')
#
# predict = load_model.predict(tomldata('ENFJ','남자','20대','무직',1))
#
# print(predict[0])

# print(tomldata('ENFJ','남자','20대','무직',3))