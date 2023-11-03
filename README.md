# Coffee Machine Program ☕

Welcome to the Coffee Machine Program, a Python project that simulates a coffee machine, allowing the user to select and enjoy their favorite coffee beverages. This program is designed to meet various user requirements, from ordering coffee to checking resources, processing coins, and making coffee.

## Purpose

The Coffee Machine Program serves a dual purpose:

1. **Learning Python**: Practicing Python, working with functions, dictionaries and more.
2. **Implementing Specific Requirements**: The program is designed to meet a set of specific requirements within a real-world app.

## Features

### 1. Ordering Coffee

The program prompts the user, asking them to choose a coffee from the available options: "espresso," "latte," or "cappuccino." The program prompts this questions after specific actions.

### 2. Turning Off the Coffee Machine

The user has the option to "turn-off" the coffee machine by typing in "off". The program ends its execution.

### 3. Printing a Report

The user can check the current status of the coffee machine's resources by entering "report." The program will generate a report that displays the current resource values, including:

- Water: [ml]
- Milk: [ml]
- Coffee: [g]
- Money: $[amount]

### 4. Resource Availability

Before processing the coffee order, the program checks if there are enough resources to make the selected drink. If any resource, such as water, milk, or coffee, is insufficient, the program will prompt the user, for example, "Sorry, there is not enough water."

### 5. Processing Coins

If the resources are sufficient, the user will be prompted to insert coins. The program accepts quarters, dimes, nickels, and pennies, with their respective values:

- Quarters: $0.25
- Dimes: $0.10
- Nickels: $0.05
- Pennies: $0.01

The program calculates the total monetary value of the coins inserted by the user.

### 6. Transaction Verification

The program checks whether the user has inserted enough money to purchase their selected drink. If the funds are insufficient, it will display a message like "Sorry, that's not enough money. Money refunded."

If the user has inserted the correct amount, the cost of the drink will be deducted from the machine's profit, which will be reflected in the next "report."

In case the user inserted too much money, the program will offer change, rounded to two decimal places. For example, "Here is $2.45 in change."

### 7. Making Coffee

Assuming the transaction is successful, and there are enough resources to make the drink, the program will deduct the necessary ingredients from the coffee machine's resources. For instance, if the user orders a latte, the program will deduct the required amount of water, milk, and coffee grounds.

Once all the resources have been deducted, the user is prompted with "Here is your drink. Enjoy!".

Enjoy your coffee with the Coffee Machine Program! 👌
