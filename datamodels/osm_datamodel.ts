// REF: https://wiki.openstreetmap.org/wiki/Key:material
enum OSM_Material {
    Wood,
    Concrete,
    Metal,
    Stone,
}

// REF: https://wiki.openstreetmap.org/wiki/Key:direction
enum OSM_Cardinal {
    N, NNE, NE, ENE, E, ESE, SE, SSE, S, SS, SW, WSW, W, WNW, NW, NNW
}

// REF: https://wiki.openstreetmap.org/wiki/Key:bench:type
enum OSM_Bench_Type {
    Seated,
    Stand_up,
    Block,
    Lounger,
    Platform,
    Swing,
    Log,
    Dangle_bench
}

// REF: https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbench
type OSM_Bench = {
    id?: number,
    type?: OSM_Bench_Type,
    backrest?: boolean,
    armrest?: boolean,
    seats?: number,
    material?: OSM_Material,
    colour?: string
    direction?: number | OSM_Cardinal,
    side?: "right" | "left" | "both",
    two_sided?: boolean,
    length?: number,
    covered?: boolean,
    operator?: string,
    historic?: "memorial",
    memorial?: "bench",
    inscription?: string,
    wheelchair?: string
}