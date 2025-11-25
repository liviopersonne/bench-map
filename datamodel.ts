enum Material {}

type Bench = {
    xcoord: number,
    ycoord: number,
    backrest?: boolean,
    picnic?: boolean,
    covered?: boolean,
    material?: Material,
    pov?: ImageData,
}