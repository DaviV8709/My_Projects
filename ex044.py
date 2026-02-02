red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
cyan = '\033[1;36m'
gray = '\033[1;37;40m'
none = '\033[m'
print('{}Challenge of paying methods{}'.format(purple, none ))
price = float(input('Enter the {}price{} of the {}product{}: '
                    .format(green, none, blue, none )))
print('There are two principal methods for pay ({}choose one{}):\n'
      '{}[ 1 ]{} - CASH/ CHECK | {}10% OFF{}\n'
      '{}[ 2 ]{} - OPTIONS WITH CARD'.format(cyan, none, cyan, none, green, none, cyan, none, ))
choice = int(input())
if choice == 1:
    print('With this {}method{} the {}final price{} will be {}R${:.2f}{}, with a discount of {}R${:.2f}{}'
          .format(gray, none, purple, none, cyan, price*0.90, none, green, price - ( price * 0.90 ), none))
elif choice == 2:
    print('There are {}3 methods{} for pay {}with card{}, depending on the {}number of installments{}: \n'
          '{}[ 1 ]{} - WITH CARD 1X | {}5% OFF{}\n'
          '{}[ 2 ]{} - WITH CARD 2X | {}SAME PRICE{}\n'
          '{}[ 3 ]{} - WITH CARD 3X OR MORE | {}20% OF INTEREST FOR EACH INSTALLMENT{}'
          .format(purple, none, purple, none, purple, none, cyan, none, green, none, cyan, none, yellow, none, cyan, none, red, none ))
    choice2 = int(input())
    if choice2 == 1:
        print('With this {}method{} the {}final price{} will be {}R${:.2f}{}, with a discount of {}R${:.2f}{}'
         .format(gray, none, purple, none, cyan, price*0.95, none, green, price - ( price * 0.95 ), none ))
    elif choice2 == 2:
        print('With this {}method{} the {}final price{} will be {}R${:.2f}{}. With two installments of {}R${:.2f}{}, {}without discount{}'
          .format(gray, none, purple, none, cyan, price, none, yellow, price /2, none, red, none ))
    elif choice2 == 3:
        time = int(input('How many {}installments{}: '. format(green, none )))
        if time == 2 or time == 1:
            print('{}Restart{}! And {}Put other number{} of {}installment{}!'
                  .format(red, none, purple, none, yellow, none ))
        else:
            tx = time * 0.20
            print('With this {}method{} the {}final price{} will be {}R${:.2f}{}. With {}{}{} installments of {}R${:.2f}{}\n'
                  'with a add of {}R${:.2f}{}'
                  .format(gray, none, purple, none, cyan, (price + (price * tx)), none, blue, time, none, blue, ((price + (price * tx)) / time), none, red, ((price + (price * tx)) - price) , none ))
else:
    print('This {}option does not exist{}! {}Try Again{}!'
          .format(red, none, purple, none ))