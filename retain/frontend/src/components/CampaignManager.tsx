import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CampaignManager = () => {
    const [campaigns, setCampaigns] = useState([]);
    const [newCampaign, setNewCampaign] = useState('');
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchCampaigns();
    }, []);

    const fetchCampaigns = async () => {
        try {
            const response = await axios.get('/api/campaigns');
            setCampaigns(response.data);
        } catch (error) {
            console.error('Error fetching campaigns:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleCreateCampaign = async () => {
        if (!newCampaign) return;

        try {
            const response = await axios.post('/api/campaigns', { name: newCampaign });
            setCampaigns([...campaigns, response.data]);
            setNewCampaign('');
        } catch (error) {
            console.error('Error creating campaign:', error);
        }
    };

    if (loading) {
        return <div>Loading campaigns...</div>;
    }

    return (
        <div>
            <h2>Campaign Manager</h2>
            <input
                type="text"
                value={newCampaign}
                onChange={(e) => setNewCampaign(e.target.value)}
                placeholder="New Campaign Name"
            />
            <button onClick={handleCreateCampaign}>Create Campaign</button>
            <ul>
                {campaigns.map((campaign) => (
                    <li key={campaign.id}>{campaign.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default CampaignManager;