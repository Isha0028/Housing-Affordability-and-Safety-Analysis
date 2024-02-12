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
➢ Loop Over Iterations: For each iteration:

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

DATASET DESCRIPTION:
⮚ "BldgType" typically refers to the type of building. It is a
categorical variable that describes the general structure or style of
the dwelling. The values in the "BldgType" column of your dataset
would indicate the kind of building each data point represents.
Common values for "BldgType" in housing datasets might include:
Single-family detached: Indicates that the building is a standalone
house, not attached to any other structure.
Two-family conversion: The building is divided into two separate
living units, often referred to as a duplex.
Townhouse inside unit: The building is part of a row of attached
houses, and this specific unit is located inside the row.
Townhouse end unit: Similar to the "Townhouse inside unit," but
this unit is located at the end of the row.
Duplex: The building is designed to house two separate living units.
Understanding the building type can be important in housing
analysis, as different types of buildings may have distinct
characteristics and can be associated with different housing market
dynamics.
⮚ "MSSubClass" typically refers to the building class. It is a
categorical variable that represents the type of dwelling involved in
the sale. The values in the "MSSubClass" column of your dataset
would indicate the class or type of each building in the dataset.
For example, in a dataset using "MSSubClass," you might
encounter values like:

20: 1-STORY 1946 & NEWER ALL STYLES
30: 1-STORY 1945 & OLDER
40: 1-STORY W/FINISHED ATTIC ALL AGES
45: 1-1/2 STORY - UNFINISHED ALL AGES
50: 1-1/2 STORY FINISHED ALL AGES
60: 2-STORY 1946 & NEWER
70: 2-STORY 1945 & OLDER
80: SPLIT OR MULTI-LEVEL
85: SPLIT FOYER
90: DUPLEX - ALL STYLES AND AGES
120: 1-STORY PUD (Planned Unit Development) - 1946 &
NEWER
... and so on.
⮚ "MSZoning" typically refers to the general zoning classification of
the property. Zoning is a set of regulations that dictate how land can
be used and what can be built on it. The "MSZoning" column in your
dataset would contain categorical values indicating the zoning
classification for each property.
Common values for "MSZoning" in housing datasets might include:
A: Agriculture
C: Commercial
FV: Floating Village Residential
I: Industrial
RH: Residential High Density
RL: Residential Low Density
RP: Residential Low Density Park
RM: Residential Medium Density
⮚ "LotConfig" typically refers to the configuration of the lot on which
a property is located. The values in the "LotConfig" column of your
dataset would indicate how the property's lot is situated in relation
to its surroundings.
Common values for "LotConfig" in housing datasets might include:
Inside: The property is located inside a subdivision and is not at the
edge of the subdivision boundary.
Corner: The property is located at the corner of two streets.

CulDSac: The property is located at the end of a cul-de-sac, which
is a dead-end street with a circular turnaround.
FR2 (Frontage on two sides of property): The property has frontage
on two sides of the lot.
FR3 (Frontage on three sides of property): The property has
frontage on three sides of the lot.

⮚ "OverallCond" typically refers to the overall condition of a
property. The "OverallCond" column in your dataset would contain
values indicating the general state or condition of each property.
Commonly, the values for "OverallCond" are on a numerical scale,
often ranging from 1 to 10, where:
1: Very Poor
2: Poor
3: Fair
4: Below Average
5: Average
6: Above Average
7: Good
8: Very Good
9: Excellent
10: Very Excellent
⮚ "YearBuilt" typically refers to the year when a property was
constructed or built. The "YearBuilt" column in your dataset would
contain the year of construction for each property.
⮚ "YearRemodAdd" typically refers to the year a property was last
remodeled or had additions made.
⮚ "Exterior1st" typically refers to the primary exterior covering or
material of a property. The "Exterior1st" column in your dataset
would contain values indicating the material used for the primary
exterior of each property.Common values for "Exterior1st" in
housing datasets might include:
VinylSd: Vinyl Siding
HdBoard: Hard Board

MetalSd: Metal Siding
Wd Sdng: Wood Siding
Plywood: Plywood
CemntBd: Cement Board
BrkFace: Brick Face
➢ "BsmtFinSF2" typically refers to the finished square footage
of the basement area, specifically for a second type of finished
space.
➢ "TotalBsmtSF" typically refers to the total finished and
unfinished square footage of the basement area in a property.
➢ "SalePrice" typically refers to the sale price of a property. The
"SalePrice" column in your dataset would contain numerical
values representing the final sale price of each property.

Conclusion:
We will be developing a real estate website where customer can see sign
in with there email id and password , they will then search on what location
they are willing to purchase the house then our website will show the crime
rate in that area and also the pricing of the houses will vary in coming
future our website will predict the real time crime rate and future crime rate
of that location and also the variation in the house pricing that will come
in future.
