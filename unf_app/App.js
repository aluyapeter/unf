import { useState } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

export default function App() {
  const [status, setStatus] = useState('Waiting to test...');

  const testConnection = async () => {
    try {
      const apiUrl = process.env.EXPO_PUBLIC_API_URL;
      const response = await fetch(`${apiUrl}/health`);
      const data = await response.json();
      setStatus(`Success: ${data.message}`);
    } catch (error) {
      setStatus(`Failed: Could not reach backend.`);
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>{status}</Text>
      <Button title="Test Connection" onPress={testConnection} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  text: { fontSize: 18, marginBottom: 20, textAlign: 'center', padding: 20 }
});