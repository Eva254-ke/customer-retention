import React, { useEffect, useState } from 'react';
import { fetchChurnStats, fetchCampaigns } from '../services/api';
import ChurnStats from './ChurnStats';
import CampaignManager from './CampaignManager';

const Dashboard: React.FC = () => {
    const [churnStats, setChurnStats] = useState(null);
    const [campaigns, setCampaigns] = useState([]);

    useEffect(() => {
        const loadData = async () => {
            const stats = await fetchChurnStats();
            const campaignsData = await fetchCampaigns();
            setChurnStats(stats);
            setCampaigns(campaignsData);
        };

        loadData();
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            {churnStats && <ChurnStats stats={churnStats} />}
            <CampaignManager campaigns={campaigns} />
        </div>
    );
};

export default Dashboard;