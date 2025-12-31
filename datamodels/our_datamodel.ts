enum Material {
    Wood,
    Concrete,
    Metal,
    Stone,
}

enum BenchType {
    Normal,
    BusStop,
    Picnic,
}

type Bench = {
    lat: number,
    lon: number,
    backrest?: boolean,
    material?: Material,
    seats?: number,
    type?: BenchType,
    covered?: boolean,
    pov?: ImageData,
}