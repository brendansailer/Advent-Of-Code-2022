// See https://aka.ms/new-console-template for more information

string[] input = File.ReadAllLines("../input.txt");

int running_total = 0;
List<int> elfs = new List<int>();

for(int i = 0; i < input.Length; i++) {
    String line = input[i];
    if(line == "") {
        elfs.Add(running_total);
        running_total = 0;
    }
    else {
        running_total += int.Parse(line);
    }
}

int part1 = elfs.Max();

elfs.Sort();
int part2 = (elfs[elfs.Count - 1] + elfs[elfs.Count - 2] + elfs[elfs.Count - 3]);

Console.WriteLine("Part 1: {0}", part1);
Console.WriteLine("Part 2: {0}", part2);