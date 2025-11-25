enum Material {
    Wood,
    Metal,
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