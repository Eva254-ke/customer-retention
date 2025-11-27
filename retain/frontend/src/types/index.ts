export interface User {
    id: string;
    name: string;
    email: string;
    phone: string;
    preferences: UserPreferences;
}

export interface UserPreferences {
    receiveSMS: boolean;
    language: string;
}

export interface ChurnPrediction {
    userId: string;
    riskScore: number;
    message: string;
}

export interface Campaign {
    id: string;
    name: string;
    startDate: Date;
    endDate: Date;
    targetAudience: string[];
    status: 'active' | 'inactive';
}