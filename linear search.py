def                                    LinearsearchProduct(productlist, targetproduct):
 indices = []

 for index,product in enumerate                    (productlist):
    if product == targetproduct:
     indices.append(index)
    
 return indices 

#Example usage:
products=("shoes","boat","coater","shoes","sandel","shoes")
target="shoes"
result=LinearsearchProduct(products,target)
print(result)