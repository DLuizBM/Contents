package StreamsAPI.Reduce202;

public class Mean {
    
    private double total;
    private double numbers;

    public Mean add(double grade){
        total += grade;
        numbers++;
        return this;
    }

    public double getValue(){
        return total / numbers;
    }

    public static Mean getMeanMatch(Mean m1, Mean m2){
        Mean meanMatch = new Mean();
        meanMatch.total = m1.total + m2.total;
        meanMatch.numbers = m1.numbers + m2.numbers;
        return meanMatch;
    }

}
