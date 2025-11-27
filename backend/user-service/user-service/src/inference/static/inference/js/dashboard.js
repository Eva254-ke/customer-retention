/**
 * Dashboard Application - Customer Retention Platform
 * Alpine.js based SPA for managing retention services
 */

function dashboardApp() {
    return {
        // Navigation state
        currentView: 'inference',
        sidebarOpen: false,

        // Auth state
        auth: {
            user: null,
            form: { username: '', token: '' },
            loading: false,
            error: null
        },

        // Services status
        services: {
            gemini: true,
            sms: true,
            auth: true
        },

        // Inference module
        inference: {
            form: {
                user_id: '',
                phone_number: '',
                engagement_score: 0.5,
                last_active_days: 7,
                extraRaw: ''
            },
            loading: false,
            error: null,
            rawError: null,
            errors: {},
            result: {
                churn_risk: null,
                retention_message: '',
                sms: null
            }
        },

        // SMS module
        sms: {
            form: { phone_number: '', message: '', async: false },
            loading: false,
            result: null
        },

        // Users module
        users: {
            list: [],
            loading: false,
            error: null
        },

        // Initialize app
        init() {
            this.loadAuthFromStorage();
            this.checkServices();
        },

        // Load auth from localStorage
        loadAuthFromStorage() {
            const savedAuth = localStorage.getItem('retention_auth');
            if (savedAuth) {
                try {
                    this.auth.user = JSON.parse(savedAuth);
                } catch (e) {
                    localStorage.removeItem('retention_auth');
                }
            }
        },

        // Check service health
        async checkServices() {
            try {
                const resp = await fetch('/api/communications/status/');
                this.services.sms = resp.ok;
            } catch {
                this.services.sms = false;
            }
        },

        // Get page title based on current view
        getPageTitle() {
            const titles = {
                inference: 'Churn Prediction',
                sms: 'SMS Messaging',
                users: 'Customer Management',
                analytics: 'Analytics',
                status: 'Service Status',
                login: 'Sign In'
            };
            return titles[this.currentView] || 'Dashboard';
        },

        // Auth methods
        async login() {
            if (!this.auth.form.username || !this.auth.form.token) {
                this.auth.error = 'Please fill in all fields';
                return;
            }

            this.auth.loading = true;
            this.auth.error = null;

            // Simulate auth (replace with real API call)
            setTimeout(() => {
                this.auth.user = {
                    name: this.auth.form.username,
                    token: this.auth.form.token
                };
                localStorage.setItem('retention_auth', JSON.stringify(this.auth.user));
                this.auth.loading = false;
                this.auth.form = { username: '', token: '' };
                this.currentView = 'inference';
            }, 500);
        },

        logout() {
            this.auth.user = null;
            localStorage.removeItem('retention_auth');
            this.currentView = 'login';
        },

        // Inference methods
        applyPreset(type) {
            const presets = {
                high: {
                    engagement_score: 0.1,
                    last_active_days: 30,
                    extraRaw: '{"rides_last_30_days": 0, "segment": "churned"}'
                },
                medium: {
                    engagement_score: 0.4,
                    last_active_days: 14,
                    extraRaw: '{"rides_last_30_days": 3, "segment": "at_risk"}'
                },
                low: {
                    engagement_score: 0.8,
                    last_active_days: 2,
                    extraRaw: '{"rides_last_30_days": 10, "segment": "loyal"}'
                }
            };

            const preset = presets[type];
            if (preset) {
                this.inference.form.engagement_score = preset.engagement_score;
                this.inference.form.last_active_days = preset.last_active_days;
                this.inference.form.extraRaw = preset.extraRaw;
            }
        },

        validateInference() {
            this.inference.errors = {};
            this.inference.error = null;
            this.inference.rawError = null;

            if (!this.inference.form.user_id.trim()) {
                this.inference.errors.user_id = 'Customer ID is required';
            }

            if (this.inference.form.extraRaw.trim()) {
                try {
                    JSON.parse(this.inference.form.extraRaw);
                } catch (e) {
                    this.inference.errors.extraRaw = 'Invalid JSON format';
                }
            }

            return Object.keys(this.inference.errors).length === 0;
        },

        buildInferencePayload() {
            let features = {
                engagement_score: Number(this.inference.form.engagement_score) || 0,
                last_active_days: Number(this.inference.form.last_active_days) || 0
            };

            if (this.inference.form.phone_number.trim()) {
                features.phone_number = this.inference.form.phone_number.trim();
            }

            if (this.inference.form.extraRaw.trim()) {
                try {
                    const extra = JSON.parse(this.inference.form.extraRaw);
                    if (extra && typeof extra === 'object') {
                        features = { ...features, ...extra };
                    }
                } catch (e) {
                    // Handled in validation
                }
            }

            return {
                user_id: this.inference.form.user_id.trim(),
                features
            };
        },

        async runInference() {
            if (!this.validateInference()) return;

            this.inference.loading = true;
            this.inference.error = null;
            this.inference.rawError = null;
            this.inference.result = { churn_risk: null, retention_message: '', sms: null };

            try {
                const resp = await fetch('/api/inference/predict/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        ...(this.auth.user?.token && { 'Authorization': this.auth.user.token })
                    },
                    body: JSON.stringify(this.buildInferencePayload())
                });

                const data = await resp.json().catch(() => ({}));

                if (!resp.ok) {
                    this.inference.error = data.error || `Request failed with status ${resp.status}`;
                    this.inference.rawError = JSON.stringify(data, null, 2);
                } else {
                    this.inference.result = {
                        churn_risk: data.churn_risk ?? null,
                        retention_message: data.retention_message || '',
                        sms: data.sms || null
                    };
                }
            } catch (e) {
                this.inference.error = 'Network error. Please check your connection.';
                this.inference.rawError = String(e);
            } finally {
                this.inference.loading = false;
            }
        },

        // Risk display helpers
        getRiskClass(risk) {
            if (risk === null) return '';
            if (risk > 0.6) return 'risk-high';
            if (risk > 0.3) return 'risk-medium';
            return 'risk-low';
        },

        getRiskBadgeClass(risk) {
            if (risk === null) return 'badge-neutral';
            if (risk > 0.6) return 'badge-error';
            if (risk > 0.3) return 'badge-warning';
            return 'badge-success';
        },

        getRiskLevel(risk) {
            if (risk === null) return 'Unknown';
            if (risk > 0.6) return 'High Risk';
            if (risk > 0.3) return 'Medium Risk';
            return 'Low Risk';
        },

        getRiskLabel(risk) {
            if (risk === null) return '';
            if (risk > 0.6) return 'Immediate attention needed';
            if (risk > 0.3) return 'Monitor closely';
            return 'Customer is engaged';
        },

        formatRisk(risk) {
            if (risk === null) return '-';
            return `${(risk * 100).toFixed(1)}%`;
        },

        // SMS methods
        async sendDirectSMS() {
            if (!this.sms.form.phone_number || !this.sms.form.message) {
                this.sms.result = { error: 'Phone number and message are required' };
                return;
            }

            this.sms.loading = true;
            this.sms.result = null;

            try {
                const resp = await fetch('/api/communications/send-sms/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        ...(this.auth.user?.token && { 'Authorization': this.auth.user.token })
                    },
                    body: JSON.stringify({
                        phone_number: this.sms.form.phone_number,
                        message: this.sms.form.message,
                        async: this.sms.form.async
                    })
                });

                const data = await resp.json().catch(() => ({}));

                if (!resp.ok) {
                    this.sms.result = { error: data.error || 'Failed to send SMS' };
                } else {
                    this.sms.result = {
                        status: data.status,
                        message_id: data.message_id,
                        task: data.task
                    };
                    // Clear form on success
                    this.sms.form.message = '';
                }
            } catch (e) {
                this.sms.result = { error: 'Network error. Please try again.' };
            } finally {
                this.sms.loading = false;
            }
        },

        // Users methods
        async loadUsers() {
            this.users.loading = true;
            this.users.error = null;

            try {
                const resp = await fetch('/api/users/', {
                    headers: {
                        ...(this.auth.user?.token && { 'Authorization': this.auth.user.token })
                    }
                });

                if (!resp.ok) {
                    throw new Error(`HTTP ${resp.status}`);
                }

                const data = await resp.json();
                this.users.list = Array.isArray(data) ? data : (data.results || []);
            } catch (e) {
                this.users.error = 'Failed to load customers';
                this.users.list = [];
            } finally {
                this.users.loading = false;
            }
        }
    };
}
