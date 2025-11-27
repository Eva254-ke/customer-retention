import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ChurnStats: React.FC = () => {
    const [churnData, setChurnData] = useState<any[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchChurnData = async () => {
            try {
                const response = await axios.get('/api/churn-stats'); // Adjust the endpoint as necessary
                setChurnData(response.data);
            } catch (err) {
                setError('Failed to fetch churn data');
            } finally {
                setLoading(false);
            }
        };

        fetchChurnData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div>
            <h2>Churn Statistics</h2>
            <table>
                <thead>
                    <tr>
                        <th>User ID</th>
                        <th>Churn Risk</th>
                        <th>Last Active</th>
                    </tr>
                </thead>
                <tbody>
                    {churnData.map((user) => (
                        <tr key={user.id}>
                            <td>{user.id}</td>
                            <td>{user.churnRisk}</td>
                            <td>{new Date(user.lastActive).toLocaleDateString()}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ChurnStats;