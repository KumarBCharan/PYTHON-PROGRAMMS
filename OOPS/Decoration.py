def sagar(args):
    def inner():
        print("sagar will starts speaking")
        args()
        print("sagar will ends speaking")
    return inner
@sagar
def vasavi():
    print("vasavi started speaking")
    print("vasavi ended speaking")

@sagar
def jaya():
    print("jaya started speaking")
    print("jaya ended speaking")
vasavi()
jaya()
