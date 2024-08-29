import json
import requests

def load_negotiation_details(file_path):
    """Load negotiation details from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def approve_negotiation(negotiation_details):

    """Send a request to approve a negotiation based on provided details."""
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJzdWIiOiJnYWlhbi5jb20iLCJ1c2VyX25hbWUiOiJwb3J0YWxfdGVzdCIsInNjb3BlIjpbInRydXN0IiwicmVhZCIsIndyaXRlIl0sInRlbmFudElkIjoiNjExYmRkMzQyNmE5NDg2MDA1NjkzYjExIiwiaXNzIjoiZ2FpYW4uY29tIiwidXNlck5hbWUiOiJwb3J0YWxfdGVzdCIsImF1dGhvcml0aWVzIjpbIlJPTEVfT01OSV9DT05TVU1FUiIsIlJPTEVfTUFSS0VUUExBQ0VfVVNFUiIsIlJPTEVfT01OSV9VU0VSIl0sImp0aSI6IjgxODE1ZDNmLTY1MTAtNDJkNC05NWZkLTNiZTJmMWYzYjg5ZiIsImVtYWlsIjoicG9ydGFsX3Rlc3RAZ2F0ZXN0YXV0b21hdGlvbi5jb20iLCJjbGllbnRfaWQiOiJnYWlhbiJ9.Mz1gWLt1rujlQWW3SzuwtERk1i6HwG9utVuMUnL-RX4kKtR1jl0eR9MZmNjRZ0znbrr6w8MOj2aAULtpIEYmM9jU_mXGBuqetPIbTuV2d4Hkv6f0qaJZLAIAU3qhgijQI9O4a2yg_rmHnibNhEcZMKEFK5AXw8M_B8XIgnNYlXDkpjEqP6Siv0HJmHA3T1j1XY8PCsluzIwDzIgRr-xqAJcaCnUwGR7XxsF-X0plk8L9qV1Z3bF2EMqqBsednYeqaM3EqwJXk27R5PFU7jn5aOc-_n9DxaGLcuJB5JoqoGW7DeaIKLzMwxvS9vP_bc8vDOxl8xk-zTRAq8goyHV6IQ',
        'Content-Type': 'application/json'
    }
    url = f"{negotiation_details['base_url']}/{negotiation_details['negotiation_id']}/approve-reject/seller/{negotiation_details['buyer_id']}/status/{negotiation_details['status']}"
    response = requests.get(url, headers=headers)
    return response
    
def main():
    # Load negotiation details
    negotiation_details = load_negotiation_details('buyer.json')
    all_responses = [] 
    # Iterate over each negotiation detail in the list
    for index, negotiation_detail in enumerate(negotiation_details):
        response = approve_negotiation(negotiation_detail)
        if response.status_code == 200:
            response_data = response.json()
            response_data['status'] = 'success' if negotiation_detail['status'] == 'APPROVED_BY_PARTIES' else 'REJECTED_BY_PARTIES'
            all_responses.append(response_data)
            print(f"Negotiation {index + 1} approved successfully.")
        else:
            # Collect error details for unsuccessful negotiations
            error_info = {
                'status': 'failure',
                'error': response.text,
                'http_status_code': response.status_code,
                'negotiation_index': index + 1
            }
            all_responses.append(error_info)
            print(f"Failed to approve negotiation {index + 1}: {response.status_code} - {response.text}")

    # Save all responses to a single JSON file
    with open('response.json', 'w') as file:
        json.dump(all_responses, file, indent=4)

if __name__ == '__main__':
    main()