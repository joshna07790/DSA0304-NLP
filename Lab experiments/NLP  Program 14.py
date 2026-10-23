def check_agreement(subject, verb):
    singular = {"he", "she", "it"}
    plural = {"they", "we", "you"}

    if subject in singular and verb == "runs":
        print("Agreement correct")
    elif subject in plural and verb == "run":
        print("Agreement correct")
    elif subject == "I" and verb == "run":
        print("Agreement correct")
    else:
        print("Agreement incorrect")

check_agreement("he", "runs")
check_agreement("they", "run")
check_agreement("he", "run")
