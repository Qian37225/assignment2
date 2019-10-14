import matplotlib.pyplot as plt
import pandas

def plot_learning_curve(iterations, train_scores, test_scores, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    plt.ylim((.2, 0.9))
    
    # if datasetNum == 1:
    #     plt.ylim((.55, 1.01))

    plt.xlabel("# Iterations")
    plt.ylabel("ACC Score")
    
    plt.grid()
    
    plt.plot(iterations, train_scores,  color="r",
             label="Training score")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(iterations, test_scores,  color="g",
             label="Test Score")

    plt.legend(loc="best")
    return plt


def plot_mse(iterations, train_scores, test_scores, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    plt.ylim((0.06,0.2))
    
    # if datasetNum == 1:
    #     plt.ylim((.55, 1.01))

    plt.xlabel("# Iterations")
    plt.ylabel("MSE")
    
    plt.grid()
    
    plt.plot(iterations, train_scores,'o-',  color="r",
             label="Training score")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(iterations, test_scores, 'o-', color="g",
             label="Test Score")

    plt.legend(loc="best")
    return plt





def plot_timing_curve(iterations, timeDuration, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    # plt.ylim((.3, 1.01))
    
    # if datasetNum == 1:
    #     plt.ylim((.55, 1.01))

    plt.xlabel("# Iterations")
    plt.ylabel("Training Time (s)")
    
    plt.grid()
    
    plt.plot(iterations, timeDuration, 'o-', color="r",
             label="Duration")

    plt.legend(loc="best")
    return plt



df = pandas.read_csv('BACKPROP_LOG.csv')
title  = 'BACKPROP '
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()   

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('RHC_LOG.csv')
title  = 'RHC'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('SA_100000000.0_0.35_LOG.csv')
title  = 'SA 0.35'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('SA_100000000.0_0.15_LOG.csv')
title  = 'SA 0.15'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()
df = pandas.read_csv('SA_100000000.0_0.55_LOG.csv')
title  = 'SA 0.55'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('SA_100000000.0_0.7_LOG.csv')
title  = 'SA 0.75'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('SA_100000000.0_0.95_LOG.csv')
title  = 'SA 0.95'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('GA_50_10_10_LOG.csv')
title  = 'GA 10-10'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('GA_50_10_20_LOG.csv')
title  = 'GA 10-20'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('GA_50_20_10_LOG.csv')
title  = 'GA 20-10'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

df = pandas.read_csv('GA_50_20_20_LOG.csv')
title  = 'GA 20-20'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()





