# Housing-Affordability-and-Safety-Analysis

Problem Statement:
Acquiring a house with all essential amenities has become a challenging
endeavour due to the alarming surge in housing prices. While there are
various market incentives aimed at helping consumers fulfill their
homeownership dreams, it is vital to understand the role of behavioural
factors in purchasing decisions. The primary objective of this project is to
analyse crime data and forecast the future crime rate in a specific area.
Additionally, we aim to predict house prices, considering various
influencing factors, such as the crime rate in the area. Our goal is to
examine the relationship between these variables and provide valuable
insights into housing affordability and security in the region.

DATA SET USED:
1) Baltimore Crime Data- Dataset is used for mapping crime of that
area where the customer is purchasing the house
1) House price prediction data- Another dataset is used to make house
pricing predictions for the same area . We have used used the
dataset of 2020 , 2021 , 2022.

ALGORITHM USED (Gradient Descent):
➢ Initialize Model Parameters: theta represents the model
parameters (coefficients) that the algorithm will adjust to make
better predictions.

➢ Learning Rate: alpha is like the step size in a game. It determines
how big of a step we take when adjusting the parameters. Too
large a step might overshoot the best values, and too small might
take too long.

➢ Number of Iterations (iters): This is how many times we're going
to adjust the parameters. Each iteration is like going through the
dataset and making a small improvement to our model.

➢ Regularization (lam): It's a penalty term to prevent the model from
becoming too complex. It helps prevent overfitting, where the
model fits the training data too closely but doesn't generalize well
to new data.

➢ Calculate Predictions (X @ theta.T): Use the current parameters
to make predictions for the training data.

➢ Calculate Error (X @ theta.T - y): Compare predictions with the
actual values to see how far off we are.

➢ Update Parameters (theta): Adjust the parameters in the
direction that reduces the error, considering both the errors and
the regularization term.

➢ Return Updated Parameters (theta): After all iterations, the
algorithm returns the updated parameters that should give us a
better model.

In our project, the gradient Descent function implements the
gradient descent algorithm with regularization. It iteratively
updates the model parameters to minimize the cost function,
considering both the errors and the regularization term.
Why gradient descent ?
We have used gradient descent in the house prediction because of
it’s:
➢ Optimizing Parameters: In house price prediction, you often have a
model with parameters (like coefficients) that need to be optimized
to make accurate predictions. Gradient Descent helps find the
optimal values for these parameters by minimizing the error
between predicted and actual prices

➢ Minimizing Cost Function: Machine learning models are trained by
minimizing a cost or loss function. This function measures the
difference between the predicted values and the actual values.
Gradient Descent is an optimization algorithm that minimizes this
cost function iteratively, gradually adjusting model parameters for
better predictions.

➢ Handling Large Datasets: Gradient Descent is efficient for handling
large datasets. Instead of evaluating the entire dataset at once, it
processes small batches or even individual data points, making it
computationally feasible for big datasets.

➢ Adaptability: Gradient Descent is adaptable to different types of
regression problems, including linear regression, which is
commonly used in house price prediction. It's a versatile algorithm
that can handle a variety of models and cost functions.

➢ Regularization: In the provided code, there's an option for L2
regularization, which helps prevent overfitting. Overfitting occurs
when a model fits the training data too closely but doesn't generalize
well to new data. Regularization helps to control the complexity of
the model.

➢ Flexibility in Model Complexity: Gradient Descent allows you to
adjust the complexity of your model. By choosing appropriate
regularization parameters, you can control how much your model
relies on the training data versus generalizing to new data




