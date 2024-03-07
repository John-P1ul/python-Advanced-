from fetet import Person, echo

class System(Person):
    @echo()
    def meth(self):
        print(Person.complexion())

echo "# python-Advanced-" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/John-P1ul/python-Advanced-.git
git push -u origin main