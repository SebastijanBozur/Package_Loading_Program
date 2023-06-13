item_weight = 0
package_weight = 0
package_count = 0
unused_capacity =0
total_packages_weight =0
package_unused_capacity =0
package_unused_capacity_max =0
package_unused_capacity_number = 0
max_item_count = int(input("Please enter the max number of items to be sent: "))
for item_count in range(max_item_count):
    item_weight = int(input("Please enter your item weight(1-10kg): "))
    if item_weight ==0:
        break
    if item_weight <1 or item_weight >10:
        print("Invalid input value or over item weight limit")
        continue
    package_weight += item_weight
    total_packages_weight += item_weight
    if package_weight > 20:
        package_count += 1
        package_weight -= item_weight
        package_unused_capacity = 20 - package_weight
        if package_unused_capacity > package_unused_capacity_max:
            package_unused_capacity_number= package_count
            package_unused_capacity_max =package_unused_capacity
        package_weight = item_weight

if package_weight > 0:
    package_count += 1
    package_unused_capacity = 20 - package_weight
    if package_unused_capacity > package_unused_capacity_max:
        package_unused_capacity_number = package_count
        package_unused_capacity_max = package_unused_capacity
unused_capacity = package_count * 20 - total_packages_weight

print(f"number of packages sent: {package_count}, total weight {total_packages_weight}kg, total unused capacity {unused_capacity}kg,")
print(f"package with with most unused capacity is package #{package_unused_capacity_number} with {package_unused_capacity_max}kg")