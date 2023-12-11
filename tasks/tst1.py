class MyDataFrame:
  """
   A class to represent a DataFrame.
   Attributes:
       data (list): The data of the DataFrame.
       columns (list): The column names of the DataFrame.
   """
  def __init__(self, data, columns):
       """
       The constructor for the MyDataFrame class.
       Parameters:
           data (list): The data of the DataFrame.
           columns (list): The column names of the DataFrame.
       """
       self.data = data #instance attribute
       self.columns = columns 
  def __str__(self):
       """
       The string representation of the DataFrame.
       Returns:
           str: The string representation of the DataFrame.
       """
      # Initialize the string with the column names
       result = f'{" ".join(self.columns):8}\n'
   
      # Add the data
       for row in self.data:
        result += f'{" ".join(map(str, row)):8}\n'
   
       return result
                 
  def index(self, index):
   """
   Access a row in the DataFrame by its index.
   Parameters:
       index (int): The index of the row to access.
   Returns:
       list: The row at the specified index.
   """
   return list(self.data[index])
  

  def __getattr__(self, column_names):
        
        column_indices = []
        for column in column_names:
            column_indices.append(self.columns.index(column))
      
        return ([row[index] for index in column_indices for row in self.data])
 
    
  
  def sort(self, column_name, reverse=False):
      """
      Sort the DataFrame by a specific column.
      Parameters:
          column_name (str): The name of the column to sort by.
          reverse (bool): Whether to sort in descending order.
      """
      # Get the index of the column
      column_index = self.columns.index(column_name)
    
    # Sort the data by the specified column
      return self.data.sort(key=lambda row: row[column_index] if row[column_index]is not None else float('inf'), reverse=reverse)
  

  def __getitem__(self, column_names):
        column_indices = []
        for column in column_names:
            column_indices.append(self.columns.index(column))
        return ([[row[index] for row in self.data] for index in column_indices])
  
  
# # Initialize data to lists. 
data = [(1, 2, 3), 
        (4, None, 10), 
    (5, 1, 19)] 
# Initialize column names
columns = ['a', 'b', "c"]
# Create the MyDataFrame
df = MyDataFrame(data, columns)
# Print the DataFrame
print(df)
print(df.a)
print("********")

# print('*********')
# print(df)
print(df.index(1))

print("**********")

print(df[["a","c"]])

print("**********")

df.sort('b')
print(df)