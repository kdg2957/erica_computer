
public class Person {

	private String name;
	
	public Person(String n) {
		name = n;
	}

	public String getName() {
		return name;
	}
	
	public boolean sameName(Person p) {
		return (this.getName()).equals(p.getName());
	}
}