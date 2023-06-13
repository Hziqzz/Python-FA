# nf = open('password.txt','w')
# nf.write('1903_matjan')
# nf.write('faizal13')
# nf.write('haha@faizal213HAHA')
# nf.write('jaja')
# nf.write('ioio')
# nf.write('lalalalal')
# nf.close()

class PasswordManager:
    def __init__(self,passwords,entered_password):
        self.passwords = passwords
        self.entered_password = entered_password

    def get_new_password(self):
        new_passwords = self.passwords[-1]
        return new_passwords

    def reset_new_passwords(self):
        print(f'{self.entered_password} is not your new password.')
        if self.entered_password not in self.passwords:
            ans = input(f'Are you sure to insert {self.entered_password} in password.txt?(Yes or No only): ')
            if ans == 'yes':
                nm = open('password.txt','a')
                nm.write('\n'+ self.entered_password)
                nm.close()
                print('Your new password have been entered. Thank you.')
        else:
            print(f'Your Password : {self.entered_password} is true. You have successfully logged in.')

    def is_correct(self):
        if self.entered_password == object1.get_new_password():
            print('You have entered your new password.')
        else:
            object1.reset_new_passwords()

list_of_passwords = open('password.txt').read()
make_as_list = list_of_passwords.split()

pas = input('Please enter your new password to reset : ')
object1 = PasswordManager(make_as_list,pas)
object1.is_correct()