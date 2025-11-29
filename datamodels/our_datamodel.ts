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
    xcoord: number,
    ycoord: number,
    type?: BenchType,
    material?: Material,
    backrest?: boolean,
    covered?: boolean,
    capacity?: number,
    pov?: ImageData,
}