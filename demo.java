package project;

import java.util.Scanner;

class Customer {
    private int customerId;
    private String customerName;
    private String mobileNumber;
    private int status;

    public Customer(int customerId, String customerName, String mobileNumber) {
        this.customerId = customerId;
        this.customerName = customerName;
        this.mobileNumber = mobileNumber;
    }

    public int getCustomerId() {
        return customerId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public int getStatus() {
        return status;
    }
}

class FoodItem {
    private int itemId;
    private String itemName;
    private double price;

    public FoodItem(int itemId, String itemName, double price) {
        this.itemId = itemId;
        this.itemName = itemName;
        this.price = price;
    }

    public int getItemId() {
        return itemId;
    }

    public String getItemName() {
        return itemName;
    }

    public double getPrice() {
        return price;
    }

    public void displayItem() {
        System.out.println(itemId + ". " + itemName + " - ₹" + price);
    }
}

class Order {
    private FoodItem[] items = new FoodItem[5];
    private int count = 0;
    private Customer customer;

    public Order(Customer customer) {
        this.customer = customer;
    }

    public void addItem(FoodItem item) {
        if (count == 5) {
            System.out.println("Cannot add more than 5 items");
            return;
        }
        items[count++] = item;
        System.out.println("Added: " + item.getItemName());
    }

    public void generateBill() {
        double total = 0;
        for (int i = 0; i < count; i++) {
            total += items[i].getPrice();
        }
        if (total > 500) {
            customer.setStatus(1);
        } else {
            customer.setStatus(0);
        }
        double discount;
        if (customer.getStatus() == 1) {
            discount = total * 0.10;
        } else {
            discount = total * 0.05;
        }
        double finalBill = total - discount;
        System.out.println("\n===== BILL SUMMARY =====");
        System.out.println("Customer ID: " + customer.getCustomerId());
        System.out.println("Name: " + customer.getCustomerName());
        System.out.print("Items: ");
        for (int i = 0; i < count; i++) {
            System.out.print(items[i].getItemName());
            if (i != count - 1) System.out.print(", ");
        }
        System.out.println("\nTotal Bill: ₹" + total);
        System.out.println("Discount: ₹" + discount);
        System.out.println("Final Bill: ₹" + finalBill);
    }
}

public class demo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        FoodItem[] menu = {
                new FoodItem(1, "Pizza", 300),
                new FoodItem(2, "Burger", 150),
                new FoodItem(3, "Pasta", 250),
                new FoodItem(4, "Noodles", 200),
                new FoodItem(5, "Cold Drink", 50)
        };
        Customer customer = new Customer(1, "Aman", "7453024245");
        Order order = new Order(customer);
        System.out.println("\n===== MENU =====");
        for (FoodItem item : menu) {
            item.displayItem();
        }
        while (true) {
            System.out.println("\n1. Add Item");
            System.out.println("2. Generate Bill");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");
            int choice = sc.nextInt();
            if (choice == 1) {
                System.out.print("Enter Item ID: ");
                int id = sc.nextInt();4
                boolean found = false;
                for (FoodItem item : menu) {
                    if (item.getItemId() == id) {
                        order.addItem(item);
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    System.out.println("Invalid Item ID!");
                }
            }
            else if (choice == 2) {
                order.generateBill();
            }
            else if (choice == 3) {
                System.out.println("Thank you!");
                break;
            }
            else {
                System.out.println("Invalid choice!");
            }
        }
    }
}