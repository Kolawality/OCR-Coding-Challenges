from sklearn import tree


# Takes a string input and turns it to a 1 if 'y', else assumed 'no' and
# return a 0
def yesNo_to_binary(answer: str):
    if answer == 'y':
        return 1
    else:
        return 0


# This is effectively the dataset, 1=TRUE, 0=FALSE regarding the headers below
features = [[1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1]
            ]

# These are the target values of each of the combinations
labels = ["JavaScript", "Elm", "TypeScript", "Scala", "Python", "Go",
          "Ruby", "Swift", "Java", "Objective C", "Unity", "Rust"]

# Asks the user to describe the programming language they are looking for
# based on the features stated
front_end_web = yesNo_to_binary(input("Front-end web? ('y' or 'no'): "))
back_end_web = yesNo_to_binary(input("Back-end web? ('y' or 'no'): "))
mobile = yesNo_to_binary(input("Mobile? ('y' or 'no'): "))
game = yesNo_to_binary(input("Game? ('y' or 'no'): "))
desktop_applications = yesNo_to_binary(input("Desktop Applications? ('y' or "
                                             "'no'): "))
systems_programming = yesNo_to_binary(input("Systems Programming? ('y' or "
                                            "'no'): "))

# Creates a decision tree classifier object
clf = tree.DecisionTreeClassifier()

# Trains the decision tree classifier
clf = clf.fit(features, labels)

# Predicts the response for the test data using the variable which the user
# has previously entered. The label object is converted form a string object
print("The program you have described is {}".format("".join(clf.predict([[
                        front_end_web,
                        back_end_web,
                        mobile,
                        game,
                        desktop_applications,
                        systems_programming]]))))
