export interface WenginesGamedata {
    [id: string]: Wengine
}

export type Wengine = {
    id: string,
    name: string,
    rarity: string,
    weaponType: string,
    stats: Stats,
    effects: string[],
    imgUrl: string
}

export type Stats = {
    [id: string]: number
}