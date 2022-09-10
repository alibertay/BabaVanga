import tkinter as tk

root = tk.Tk()
root.title("BabaVanga")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

def PredictScore():
    import numpy as np
    data = np.genfromtxt('data.csv', delimiter=',')
    target = np.genfromtxt('target.csv')

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)

    X_new = np.array([[int(home.get()), int(away.get())]])
    predict = knn.predict(X_new)

    y_predict = knn.predict(X_test)
    probablity = np.mean(y_predict == y_test) * 100
    score = str(predict).replace("[", "").replace("]", "")[:-1].replace(".", " -")

    ScoreLabel = tk.Label(root, text=f"%{round(probablity, 2)} ihtimalle maçın skoru: {score}")
    canvas.create_window(200, 220, window=ScoreLabel)

HomeLabel = tk.Label(root, text="Home ELO")
canvas.create_window(200, 50, window=HomeLabel)
home = tk.Entry(root)
canvas.create_window(200, 70, window=home)

AwayLabel = tk.Label(root, text="Away ELO")
canvas.create_window(200, 120, window=AwayLabel)
away = tk.Entry(root)
canvas.create_window(200, 140, window=away)

PredictButton = tk.Button(text='Predict Score', command=PredictScore)
canvas.create_window(200, 180, window=PredictButton)

root.mainloop()


