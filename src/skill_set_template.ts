export interface char {
    id: string
    name: string
    weaponType: string
    hitType: []
    camp: string
    skillKit: SkillKit
    hitMap: HitMap
    staticStats: StaticStats
    growthStat: GrowthStat
    coreSkill: CoreSkill
}

export type StaticStats = {
    [id: string]: string
}

export type GrowthStat = {
    [id: string]: BaseGrowthStat
}

export type BaseGrowthStat = {
    base: number,
    growth: number,
    asc: number
}

export type CoreSkill = {
    desc: string,
    coreGrowthStat: CoreGrowthStat
}

export type CoreGrowthStat = {
    [id: string]: number
}

export type HitMap = {
    [id: string]: SimpleHit
}

export type SimpleHit = {
    anomalyBuildup: number,
    miasmaDepletion: number,
    dmg: number[],
    daze: number[],
}

export type SkillKit = {
    [id: string]: Skill
}

export type Skill = {
    skillId: number, //basic, dodge
    Desc: string,
    subSkills: SubSkill
}

export type SubSkill = {

    [id: string]: ComplexHitData,
}

//esse tipo terá que ser modificado caso precisarmos do stunRatio
export type ComplexHitData = {
    name: string,
    formula: string, // agrupar danos que usam multiplos simpleHits
    // anby ex = [1521008]*3 + [1521009]
    hitID: string[]
    dmg: string[], // resultado da conta dos simple hits
    daze: string[],
}

/*
"Special":{
    "EX Special Attack":{
        "DMG":"638.0%",
        "DAZE":"338.0%",
        "1521008":{
            "DMG":191.4,
            "Daze":101.4
        },
        "1521009":{
            "DMG":63.8,
            "Daze":33.8
        }

    }
} 
*/