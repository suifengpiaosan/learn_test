package Hellojava;
public class hello1 {
	int puppyage;
	public hello1(String name){
		System.out.println("小狗的名字是："+name);
		
	}
	public void setAge(int age) {
		puppyage = age;
		
	}
	public int getAge(){
		System.out.println("小狗的年龄为："+puppyage);
		return puppyage;
		
	}
	
	
	
	public static void main(String[] args){
		hello1 myHello1 = new hello1("tommy");
		myHello1.setAge(2);
		myHello1.getAge();
		
	}
		
	
}


