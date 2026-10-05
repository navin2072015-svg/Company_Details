#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:44:01 2026

@author: pgcp-esd
"""

class Person:
   
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Vendor(Person):
    def __init__(self, vendor_id, name, email, phone_number, products_supplied):
        super().__init__(name, email)
        self.vendor_id = vendor_id
        self.phone_number = phone_number
        self.products_supplied = products_supplied or []

    def display_details(self):
        print(f"\n--- Vendor Details [ID: {self.vendor_id}] ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number}")
        print(f"Products Supplied: {', '.join(self.products_supplied)}")


class Customer(Person):
    def __init__(self, cust_id, name, email, credit_class, discounts, plan_assigned):
        super().__init__(name, email)
        self.cust_id = cust_id
        self.credit_class = credit_class
        self.discounts = discounts
        self.plan_assigned = plan_assigned


class IndividualCustomer(Customer):
    def __init__(self, cust_id, name, email, credit_class, discounts, plan_assigned, phone_number):
        super().__init__(cust_id, name, email, credit_class, discounts, plan_assigned)
        self.phone_number = phone_number

    def display_details(self):
        print(f"\n--- Individual Customer Details [ID: {self.cust_id}] ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Credit Class: {self.credit_class}")
        print(f"Discounts: {self.discounts}")
        print(f"Plan Assigned: {self.plan_assigned}")
        print(f"Phone Number: {self.phone_number}")


class CompanyCustomer(Customer):
    def __init__(self, cust_id, name, email, credit_class, discounts, plan_assigned, relationship_manager, credit_line, extensions, list_of_numbers):
        super().__init__(cust_id, name, email, credit_class, discounts, plan_assigned)
        self.relationship_manager = relationship_manager
        self.credit_line = credit_line
        self.extensions = extensions or []
        self.list_of_numbers = list_of_numbers or []

    def display_details(self):
        print(f"\n--- Corporate Customer Details [ID: {self.cust_id}] ---")
        print(f"Company Name: {self.name}")
        print(f"Corporate Email: {self.email}")
        print(f"Credit Class: {self.credit_class}")
        print(f"Credit Line Amount: {self.credit_line}")
        print(f"Relationship Manager: {self.relationship_manager}")
        print(f"Plan Assigned: {self.plan_assigned}")
        print(f"Discounts Applied: {self.discounts}")
        print(f"Company Numbers: {', '.join(self.list_of_numbers)}")
        print(f"Internal Extensions: {', '.join(self.extensions)}")


def main():
    vendors = []
    customers = []

    while True:
        print("\n=== ABCTel Telecom Management System ===")
        print("1. Add a New Vendor")
        print("2. Add a New Individual Customer")
        print("3. Add a New Company Customer")
        print("4. Display All Records")
        print("5. Search Customer or Vendor by ID")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            vendor_id = input("Enter Vendor ID: ")
            name = input("Enter Vendor Name: ")
            email = input("Enter Vendor Email: ")
            phone = input("Enter Phone Number: ")
            products_in = input("Enter products supplied (separated by commas): ")
            products = [p.strip() for p in products_in.split(",") if p.strip()]

            new_vendor = Vendor(vendor_id, name, email, phone, products)
            vendors.append(new_vendor)
            print("Vendor added successfully!")

        elif choice == '2':
            cust_id = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            email = input("Enter Email: ")
            credit = input("Enter Credit Class (A/B/C): ")
            discount = input("Enter Discount %: ")
            plan = input("Enter Assigned Plan: ")
            phone = input("Enter Phone Number: ")

            new_ind = IndividualCustomer(cust_id, name, email, credit, discount, plan, phone)
            customers.append(new_ind)
            print("Individual Customer added successfully!")

        elif choice == '3':
            cust_id = input("Enter Customer ID: ")
            name = input("Enter Company Name: ")
            email = input("Enter Corporate Email: ")
            credit = input("Enter Credit Class (A/B/C): ")
            discount = input("Enter Discount %: ")
            plan = input("Enter Assigned Plan: ")
            rm = input("Enter Relationship Manager Name: ")
            credit_line = input("Enter Credit Line Limit: ")
            
            ext_in = input("Enter internal extensions (separated by commas): ")
            extensions = [e.strip() for e in ext_in.split(",") if e.strip()]
            
            nums_in = input("Enter company phone numbers (separated by commas): ")
            numbers = [n.strip() for n in nums_in.split(",") if n.strip()]

            new_comp = CompanyCustomer(cust_id, name, email, credit, discount, plan, rm, credit_line, extensions, numbers)
            customers.append(new_comp)
            print("Company Customer added successfully!")

        elif choice == '4':
            print("\n=== ALL REGISTERED VENDORS ===")
            if not vendors:
                print("No vendors registered.")
            for v in vendors:
                v.display_details()

            print("\n=== ALL REGISTERED CUSTOMERS ===")
            if not customers:
                print("No customers registered.")
            for c in customers:
                c.display_details()

        elif choice == '5':
            search_id = input("Enter ID to search: ")
            found = False

            for v in vendors:
                if v.vendor_id == search_id:
                    v.display_details()
                    found = True
                    break

            if not found:
                for c in customers:
                    if c.cust_id == search_id:
                        c.display_details()
                        found = True
                        break

            if not found:
                print("No Vendor or Customer found with that ID.")

        elif choice == '6':
            print("Exiting ABCTel System.")
            break

        else:
            print("Invalid choice. Please pick from 1 to 6.")


main()
