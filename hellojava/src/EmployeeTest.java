

public class EmployeeTest {
	public static void main(String[] args) {
		Employee empOne = new Employee("RUNOOB1");
		Employee empTwo = new Employee("RUNOOB2");
		
		empOne.empAge(26);
		empOne.empDesignation("高级工程师");
		empOne.empSalary(1000);
		empOne.printEmployee();
	}

}
