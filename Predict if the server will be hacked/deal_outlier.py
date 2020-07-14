def deal_with_outlier(column,df_name):
    Q1=df_name[column].quantile(q = 0.25)
    Q2=df_name[column].quantile(q = 0.50)
    Q3=df_name[column].quantile(q = 0.75)
    Q4=df_name[column].quantile(q = 1.00)
    print('1º Quartile: ', Q1)
    print('2º Quartile: ', Q2)
    print('3º Quartile: ', Q3)
    print('4º Quartile: ', Q4)
    #Calculate the outliers:
    IQR = Q3 - Q1  # Interquartile range, 
    Lower=Q1 - 1.5 * IQR
    Upper=Q3 + 1.5 * IQR
    print("Lower bound",Lower)
    print("Upper bound",Upper)  
    ## Flooring
    df_name.loc[df_name[column] < (Q1 - 1.5 * IQR),column] = df_name[column].quantile(0.05)
    ## Capping 
    df_name.loc[df_name[column] > (Q3 + 1.5 * IQR),column] = df_name[column].quantile(0.95)
    Boxplot=df_name.boxplot(column=[column])
    out=df_name[column].quantile(q = 0.75) + 1.5*(df_name[column].quantile(q = 0.75) - df_name[column].quantile(q = 0.25))
    print(' above: ',out , 'are outliers')
    
    
#     show the percentage of outlier for upper
    print('Number of outliers in upper: ', df_name[df_name[column] > Upper][column].count())
    print('Number of clients: ', len(df_name))
#Outliers in %
    print('Outliers are:', round(df_name[df_name[column] > Upper][column].count()*100/len(df_name),2), '%')
    
    #     show the percentage of outlier for lower
    print('Number of outliers in Lower: ', df_name[df_name[column] > Lower][column].count())
    print('Number of clients: ', len(df_name))
#Outliers in %
    print('Outliers are:', round(df_name[df_name[column] > Lower][column].count()*100/len(df_name),2), '%')
    return Boxplot
