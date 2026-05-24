exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  const { phone, otp } = JSON.parse(event.body);

  const response = await fetch('https://api.brevo.com/v3/transactionalSMS/sms', {
    method: 'POST',
    headers: {
      'api-key': process.env.BREVO_API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      sender: 'AppAbbottabad',
      recipient: phone,
      content: `Your OTP is: ${otp}`
    })
  });

  const data = await response.json();
  return {
    statusCode: 200,
    body: JSON.stringify({ success: true, data })
  };
};
