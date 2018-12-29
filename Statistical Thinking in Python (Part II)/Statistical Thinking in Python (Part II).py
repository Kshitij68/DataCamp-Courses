import matplotlib.pyplot as plt
plt.hist(inter_nohitter_time,bins = 50, normed = True, histtype = 'step')
#step makes the histogram in a step function
#normed = True: This normalizes the data
slope, intercept = np.polyfit(total_votes,dem_share,1) #np.polyfit(x,y,degree_of_the_polynomial)
a = np.linspace(0,0.1,200)#np.linspace(start,end,number_of_points)

a = np.empty(1000) #Creates an empty array of 1000 size
conf_int = np.percentile(data,[2.5,50,74]) #Value for 2.5,50 and 74th confidence is returned
bs_sample = np.random.choice(rainfall, size=len(rainfall))
#Bootstrapping is basically resampling the data for statistical inference