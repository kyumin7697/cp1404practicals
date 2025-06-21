"""
Estimate: 50 minutes
Actual:
pseudocode:
define main function
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_to_wins = count_champions(data)
    countries = get_countries(data)

    print "Wimbledon Champions:"
    for champion, wins in champion_to_wins
        print "{champion} {wins}"

    print total number of countries
    print countries in alphabetical order

define read_wimbledon_data function
data = []
    open file with utf-8-sig"
        for line in in_file
            parts = line.strip()
            champion = parts[2]
            country = parts[1]
            data.append([champion, country])
    return data

define count_champions function
champion_to_wins = {}
    for champion, i in data
        if champion in champion_to_wins
            champion_to_wins[champion] += 1
        else
            champion_to_wins[champion] = 1
    return champion_to_wins

define get_countries function
    return {country for i, country in data}
end main function
"""

