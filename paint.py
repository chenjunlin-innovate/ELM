import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [250,500,750,1000,1500,2000,3000,5000]
    y = [0.8731,0.9091,0.9284,0.9386,0.9512,0.9614,0.9704,0.9813]
    y2 = [0.8778,0.9119,0.9266,0.9394,0.9470,0.9556,0.9624,0.9685]

    y3 = [0.8718,0.9007,0.9167,0.9261,0.9375,0.9451,0.9512,0.9511]
    y4 = [0.8782,0.9064,0.9148,0.9264,0.9358,0.9382,0.9450,0.9425]

    loss1=[0.9428,0.7790,0.7056,0.6285,0.5624,0.4968,0.4349,0.3687]
    loss2=[0.9563,0.7639,0.7253,0.6614,0.5899,0.5462,0.4935,0.4234]
    loss3=[1.203,0.8418,0.7844,0.7186,0.6659,0.6198,0.5979,0.6205]
    loss4=[0.9444,0.8227,0.7650,0.7290,0.6789,0.6291,0.6054,0.6486]
    plt.plot(x, loss1,label= '$elm-train$',color="red")
    plt.plot(x, loss2,label= '$elm-test$',color="blue")
    plt.plot(x, loss3, label='$os-elm-train$')
    plt.plot(x, loss4, label='$os-elm-test$')
    plt.legend()
    plt.xlabel("point number")
    plt.ylabel("loss")
    plt.show()