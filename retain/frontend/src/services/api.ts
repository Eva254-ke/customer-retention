import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// User Service API calls
export const getUserProfile = async (userId) => {
  const response = await apiClient.get(`/users/${userId}/`);
  return response.data;
};

export const updateUserProfile = async (userId, data) => {
  const response = await apiClient.put(`/users/${userId}/`, data);
  return response.data;
};

// Event Analytics API calls
export const getEventAnalytics = async () => {
  const response = await apiClient.get('/events/analytics/');
  return response.data;
};

// AI Inference API calls
export const getChurnPrediction = async (userId) => {
  const response = await apiClient.post('/predictions/churn/', { userId });
  return response.data;
};

// Communication API calls
export const sendSMS = async (messageData) => {
  const response = await apiClient.post('/communications/sms/', messageData);
  return response.data;
};