export interface char {
    skillKit: SkillKit
    hitMap: { [id: string]: SimpleHit }
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
    energyCost: number,
    adrenalineCost: number,
    dmg: number[], // resultado da conta dos simple hits
    daze: number[],
    simpleHit: string[]
}



export type SimpleHit = {
    id: string,
    energyGain: number,
    anomalyBuildup: number,
    decibelsGain: number,
    adrenalineGain: number,
    miasmaDepletion: number,
    dmg: number[],
    daze: number[],
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