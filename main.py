import pandas as pd
from tkinter import *
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import pickle




def return_model():
    df = pd.read_csv("sms_spam.tsv", sep='\t')
    print(df.head())
    X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.3, random_state= 42)
    text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
    text_clf.fit(X_train, y_train)
    # save the model to disk
    filename = 'finalized_model.sav'
    pickle.dump(text_clf, open(filename, 'wb'))

    return text_clf

def pt():
    print(pd.DataFrame([e2.get()]))
    new_df = pd.DataFrame([e2.get()])
    passed_text =new_df.iloc[0]
    predicted = loaded_model.predict(passed_text)
    print(predicted)
    if predicted[0] == 'ham':
        e3.config(text='Not a spam' + '  🙂')
    else:
        e3.config(text='Spam' + '  😞')


window = Tk()
window.title('Spam/ Ham')
# window.geometry("300x200")

e1 = Label(window, text="enter your message")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='notspam👍     spam👎 ')

# Create the Button Widget
b1 = Button(window, text="Convert", command=pt)

# grid method is used for placing
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
b1.grid(row=0, column=2)
e3.grid(row=1, column=1, columnspan=2, padx=10, pady=20)

# loaded_model = return_model()

# load the model from disk
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))


window.mainloop()


