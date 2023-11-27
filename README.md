# Embeddings

[https://github.com/ldehner/EmbeddingsRequirementsClustering](https://github.com/ldehner/EmbeddingsRequirementsClustering)

# Durchführung

1. Embeddings mittels OpenAi API generieren
2. Embeddings speichern
3. Cluster berechnen
    1. KMeans
    2. KMeans is a popular clustering algorithm in machine learning. It is used to partition a dataset into K distinct clusters based on the similarity of data points.
    3. Hierarchical
4. Graph generieren

## **KMeans Cluster**

### RAW

```markup
Cluster 1:
  4. Each product must have a unit and a price per unit, denominated in Euros
  5. Customers place orders over the phone, providing their unique seven-digit customer number with a two-digit area code and one-digit checksum
  6. Authenticate customers over the phone and check for blacklisting.
  10. Provide an eight-digit order number with a checksum at the end of the order process
  16. Enable customers to inquire about the status of their order using the order number
  17. Allow order cancellation by phone before the order is assembled. Cancellations are irreversible, and order updates require placing a new order
  19. Enable ordering and canceling via SMS, using specific formats for product codes and order numbers

Cluster 2:
  11. Packing clerks assemble orders and place them in a paper bag
  12. Print labels and invoices with specific details, including the names of the customer and packing clerk, address, order number, and assigned delivery clerk
  14. Delivery clerks to calculate the best delivery route, often with the aid of a spreadsheet
  18. Automate current processes with a web application, supporting specific browser versions for customers, packing clerks, delivery clerks, and managers
  22. Automate the transfer of expected payment records to the existing payment system once an order is assembled
  23. Generate automatic daily business reports for managers, detailing orders, products, amounts, clerks involved, customers, addresses, and order numbers

Cluster 3:
  1. Guarantee breakfast delivery in under 25 minutes across the city
  2. Offer various prepackaged breakfast options and allow customers to assemble individual breakfasts from a list of products
  3. Support the inclusion of both simple and prepackaged products within orders
  7. Allow customers to directly name products, choose from a recommended list, or use a previous order as a blueprint to assemble their shopping cart

Cluster 4:
  15. Require customers to sign an invoice copy to confirm delivery
  20. Replace signature-based delivery confirmation with a browser-based system where customers enter a password to confirm delivery
  21. Implement a product search function accessible via a browser without the need for authentication

Cluster 5:
  8. Restrict to one blueprint order per new order, though a single order can be used as a blueprint multiple times
  9. Associate only one delivery address per customer, eliminating the need to specify it for each order
  13. Allow for multiple prints of an invoice, each with a unique copy number
```

### ChatGPT

Based on the descriptions of the requirements within each cluster, here are possible component names that capture the essence of each group:

**Cluster 1: Customer and Order Management**

- This cluster seems to focus on the identification, authentication, and management of customer orders and inquiries, as well as the handling of order cancellations and updates.

**Cluster 2: Order Processing and Logistics**

- These requirements deal with the assembly of orders, printing of necessary documentation, and automation of the order processing system, as well as handling the logistics of order delivery and payment processing.

**Cluster 3: Product Offering and Customization**

- This cluster is about the variety of breakfast options available and the flexibility for customers to customize their orders, indicating a focus on the product service offering and customization capabilities.

**Cluster 4: Delivery Confirmation and Customer Interface**

- The requirements here are centered around confirming the delivery of orders and enhancing the customer interface for order confirmation and product searching, suggesting a focus on the customer experience post-order placement.

**Cluster 5: Order Blueprint and Delivery Efficiency**

- This cluster includes requirements that streamline the ordering process by using order blueprints and associating a single delivery address with a customer, which speaks to improving the efficiency and simplicity of recurring orders and deliveries.

These component names are meant to broadly capture the functions of each cluster of requirements. They should be descriptive enough for stakeholders to understand the general scope of each component within the system.

### Graph

![Untitled](Embeddings%206cf512f4ed79429d9ded2f4ea724eff0/Untitled.png)

## **Hierarchical Cluster**

### RAW

```markup
Cluster 1:
  1. Guarantee breakfast delivery in under 25 minutes across the city
  2. Offer various prepackaged breakfast options and allow customers to assemble individual breakfasts from a list of products
  3. Support the inclusion of both simple and prepackaged products within orders
  4. Each product must have a unit and a price per unit, denominated in Euros
  7. Allow customers to directly name products, choose from a recommended list, or use a previous order as a blueprint to assemble their shopping cart
  21. Implement a product search function accessible via a browser without the need for authentication

Cluster 2:
  5. Customers place orders over the phone, providing their unique seven-digit customer number with a two-digit area code and one-digit checksum
  6. Authenticate customers over the phone and check for blacklisting.
  10. Provide an eight-digit order number with a checksum at the end of the order process
  16. Enable customers to inquire about the status of their order using the order number
  17. Allow order cancellation by phone before the order is assembled. Cancellations are irreversible, and order updates require placing a new order
  19. Enable ordering and canceling via SMS, using specific formats for product codes and order numbers

Cluster 3:
  8. Restrict to one blueprint order per new order, though a single order can be used as a blueprint multiple times
  9. Associate only one delivery address per customer, eliminating the need to specify it for each order
  13. Allow for multiple prints of an invoice, each with a unique copy number

Cluster 4:
  11. Packing clerks assemble orders and place them in a paper bag
  12. Print labels and invoices with specific details, including the names of the customer and packing clerk, address, order number, and assigned delivery clerk
  14. Delivery clerks to calculate the best delivery route, often with the aid of a spreadsheet
  18. Automate current processes with a web application, supporting specific browser versions for customers, packing clerks, delivery clerks, and managers
  22. Automate the transfer of expected payment records to the existing payment system once an order is assembled
  23. Generate automatic daily business reports for managers, detailing orders, products, amounts, clerks involved, customers, addresses, and order numbers

Cluster 5:
  15. Require customers to sign an invoice copy to confirm delivery
  20. Replace signature-based delivery confirmation with a browser-based system where customers enter a password to confirm delivery
```

### ChatGPT

Based on the hierarchical clustering of your requirements, here are suitable component names that align with the functions and focus of each cluster:

**Cluster 1: Product Management and Discovery**

- This cluster groups requirements related to product offerings, including various breakfast options, product customization, pricing units, and the ability for customers to search products online. It's focused on managing the range of products offered and facilitating customer discovery of these products.

**Cluster 2: Customer Order Interaction and Management**

- These requirements are centered around customer interactions for placing and managing orders, including order placement via phone and SMS, customer authentication, order inquiry, and cancellation. This cluster is essentially about managing the customer's journey from placing an order to making changes to it.

**Cluster 3: Order Efficiency and Streamlining**

- This cluster involves requirements that make the order process more efficient and streamlined, such as using a previous order as a blueprint, associating a single delivery address with a customer, and handling multiple invoice prints. It's focused on making the ordering process quicker and more straightforward for repeat customers.

**Cluster 4: Order Fulfillment and System Automation**

- The requirements here are about the behind-the-scenes processes of order fulfillment, including packing, labeling, route calculation for deliveries, and system automation for packing clerks and managers. This cluster emphasizes the automation and management of the order fulfillment process and back-office operations.

**Cluster 5: Delivery Confirmation and Authentication**

- This cluster deals with the final stage of the order process - confirming delivery. It involves requirements for customers to confirm delivery, either through a traditional signature or a browser-based system. This cluster focuses on ensuring that the delivery process is completed and authenticated properly.

Each of these component names provides a high-level summary of the primary functions or focus areas of the requirements in their respective clusters, aiding in understanding and communication about different parts of the system.

### Graph

![Untitled](Embeddings%206cf512f4ed79429d9ded2f4ea724eff0/Untitled%201.png)