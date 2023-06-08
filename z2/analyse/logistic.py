import numpy as np
import pandas as pd
from pandas.errors import SettingWithCopyWarning
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

from analyse import sql_select
import warnings


class Logistic_tourism():
    def test(self, test_x_in):
        warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
        ss = sql_select.sql_select()
        ss = ss.selectknn(ss.conn)

        df = pd.DataFrame(ss, columns=['用户', '出发日期', '历经时长', '城市', '景点', '拍摄数量', '标签'])

        x1 = df['出发日期']
        x2 = df['标签']
        x3 = df['历经时长']
        y = df['城市']
        new_x2, new_y = x2, y
        train_x, train_y = [], []
        for i in range(len(x1)):
            data = []
            data.append(int(str(x1[i])[5:7]))
            if x2[i] == '  ':
                new_x2[i] = new_x2[i-1].split("\xa0")[0]
            else:
                new_x2[i] = new_x2[i].split("\xa0")[0]
            data.append(new_x2[i])
            data.append(int(x3[i]))
            train_x.append(data)

            if y[i] == '   ':
                new_y[i] = new_y[i-1].split(" ")[0]
            else:
                new_y[i] = new_y[i].split(" ")[0]

            train_y.append(y[i])
        # print(train_x)
        # print(train_y)

        new_train_x = pd.DataFrame(train_x, columns=['月份', '标签', '时长'])
        new_test_x = pd.DataFrame(test_x_in, columns=['月份', '标签', '时长'])
        new_train_y = pd.DataFrame(train_y, columns=['城市'])

        label = LabelEncoder()
        label.fit(np.unique(list(new_train_x['标签'].values)+list(new_test_x['标签'].values)+list(new_train_y['城市'].values)))

        new_train_x['标签'] = label.transform(list(new_train_x['标签'].values))
        new_test_x['标签'] = label.transform(list(new_test_x['标签'].values))
        new_train_y['城市'] = label.transform(list(new_train_y['城市'].values))
        new_train_y = list(new_train_y['城市'].values)

        model = LogisticRegression(solver="sag", max_iter=1000000)
        model.fit(new_train_x, new_train_y)

        y_pred = model.predict(new_test_x)
        index = new_train_y.index(y_pred[0])
        city = train_y[index]

        return city

if __name__ == '__main__':
    lt = Logistic_tourism()
    city = lt.test([[2, '深度游', 15]])
    print(city)



