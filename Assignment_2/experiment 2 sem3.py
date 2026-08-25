import datetime

# ==========================================
# 1. DECORATORS
# ==========================================


# Function Decorator: Adds logging around function execution
def log_report(func):

  def wrapper(*args, **kwargs):
    print("\n[LOG] Starting report generation...")
    result = func(*args, **kwargs)
    print("[LOG] Report generated successfully!")
    return result

  return wrapper


# Class Decorator: Uses __call__ to modify output (converts to UPPERCASE)
class UpperFormatter:

  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    result = self.func(*args, **kwargs)
    return result.upper()


# ==========================================
# 2. MAIN REPORT CLASS
# ==========================================


class ReportGenerator:
  # Class state (shared across all instances)
  organization = "MIT ADT University"

  def __init__(self, title, content, author="Admin"):
    self.title = title
    self.content = content
    self.author = author
    self.date = datetime.datetime.now().strftime("%Y-%m-%d")

  # --- MAGIC METHODS ---

  # 1. __str__: Friendly string output for printing the object
  def __str__(self):
    return f"Report: '{self.title}' by {self.author} ({self.date})"

  # 2. __add__: Overloads the '+' operator to merge two reports
  def __add__(self, other):
    merged_title = f"{self.title} & {other.title}"
    merged_content = f"{self.content}\n---\n{other.content}"
    return ReportGenerator(merged_title, merged_content, self.author)

  # --- CLASS METHODS ---

  # Class method to change organization name across all instances
  @classmethod
  def set_org(cls, new_org):
    cls.organization = new_org

  # Class method as an alternative constructor (creates a bulleted list report)
  @classmethod
  def from_bullet_points(cls, title, points, author="Admin"):
    formatted_content = "\n".join([f"• {p}" for p in points])
    return cls(title, formatted_content, author)

  # --- REPORT METHODS ---

  @log_report
  def generate_report(self):
    return f"[{self.organization}]\nTitle: {self.title}\nAuthor: {self.author}\nDate: {self.date}\n\nContent:\n{self.content}"

  @UpperFormatter
  def generate_uppercase_report(self):
    return self.generate_report()


# ==========================================
# 3. DEMONSTRATION / EXECUTION
# ==========================================
if __name__ == "__main__":
  # Modify class state using @classmethod
  ReportGenerator.set_org("MIT ADT University - School of Computing")

  # Create regular report
  r1 = ReportGenerator(
      "Lab 1 Summary", "Completed Experiment 1 on Object-Oriented Programming."
  )

  # Create report using the class method alternative constructor
  r2 = ReportGenerator.from_bullet_points(
      "Lab 2 Tasks",
      ["Learn Decorators", "Learn Class Methods", "Learn Magic Methods"],
  )

  # 1. Demonstrating __str__ magic method
  print("--- Print Object (__str__) ---")
  print(r1)

  # 2. Demonstrating Operator Overloading (__add__)
  combined_report = r1 + r2

  # 3. Generating standard report with Function Decorator
  print("\n--- Standard Report ---")
  print(combined_report.generate_report())

  # 4. Generating report with Class Decorator
  print("\n--- Uppercase Report ---")
  print(r1.generate_uppercase_report())