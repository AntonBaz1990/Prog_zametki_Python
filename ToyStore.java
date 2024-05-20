import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;

class Toy {
    int id;
    String name;
    int frequency;

    public Toy(int id, String name, int frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getFrequency() {
        return frequency;
    }
}

public class ToyStore {

    private PriorityQueue<Toy> toyQueue;

    public ToyStore(Toy[] toys) {
        toyQueue = new PriorityQueue<>((t1, t2) -> t2.getFrequency() - t1.getFrequency());
        for (Toy toy : toys) {
            toyQueue.offer(toy);
        }
    }

    public void writeTopToysToFile(int numToys, String filename) {
        try (FileWriter fileWriter = new FileWriter(filename)) {
            for (int i = 0; i < numToys; i++) {
                Toy currentToy = toyQueue.poll();
                if (currentToy != null) {
                    fileWriter.write("ID: " + currentToy.getId() + ", Название: " + currentToy.getName() + "\n");
                    toyQueue.offer(currentToy); // Повторно добавляем игрушку в очередь
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Toy[] toys = {
                new Toy(1, "Кукла", 5),
                new Toy(2, "Машинка", 3),
                new Toy(3, "Мяч", 7)
        };

        ToyStore toyStore = new ToyStore(toys);
        toyStore.writeTopToysToFile(10, "output.txt");
    }
}
