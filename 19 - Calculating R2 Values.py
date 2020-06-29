Rsqu_test = []

order = [1, 2, 3, 4]

for n in order:
   pr = PolynomialFeatures(degree = n)
   x_train_pr = pr.fit_transform(x_train[['horsepower']])
   x_test_pr = pr.fit_transform(x_test[['horsepower']])
   lr.fit(x_train_pr, y_train)
   Rsqu_test.append(lr.score(x_test_pr, y_test))

plt.plot(order, Rsqu_test)
plt.xlabel('order')
plt.ylabel('R^2')
plt.title('R^2 Using Test Data')
plt.text(3, 0.75, 'Maximum R^2 ')    
