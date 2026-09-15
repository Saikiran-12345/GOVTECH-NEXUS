import React, { createContext, useContext, useState, useEffect } from 'react';

export interface UserRole {
  id: number;
  name: str;
  code: string;
}

export interface User {
  id: number;
  email: string;
  username: string;
  full_name: string;
  status: string;
  is_superuser: boolean;
  roles: UserRole[];
}

interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (token: string, refreshToken: string, user: User) => void;
  logout: () => void;
  hasRole: (roleCode: string) => boolean;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(() => {
    const savedUser = localStorage.getItem('govtech_user');
    return savedUser ? JSON.parse(savedUser) : null;
  });
  const [token, setToken] = useState<string | null>(() => localStorage.getItem('govtech_access_token'));

  const login = (accessToken: string, refreshToken: string, userData: User) => {
    setToken(accessToken);
    setUser(userData);
    localStorage.setItem('govtech_access_token', accessToken);
    localStorage.setItem('govtech_refresh_token', refreshToken);
    localStorage.setItem('govtech_user', JSON.stringify(userData));
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('govtech_access_token');
    localStorage.removeItem('govtech_refresh_token');
    localStorage.removeItem('govtech_user');
  };

  const hasRole = (roleCode: string): bool => {
    if (!user) return false;
    if (user.is_superuser) return true;
    return user.roles.some(r => r.code === roleCode);
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout, hasRole, isAuthenticated: !!user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within an AuthProvider');
  return context;
};
