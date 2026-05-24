exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  const { email, otp } = JSON.parse(event.body);

  const response = await fetch('https://api.brevo.com/v3/smtp/email', {
    method: 'POST',
    headers: {
      'api-key': process.env.BREVO_API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      sender: { name: 'Pakistan Prime Portal', email: 'alertprocctv@gmail.com' },
      to: [{ email: email }],
      subject: 'Your OTP Code',
      textContent: `Your OTP is: ${otp}. Valid for 10 minutes.`
    })
  });

  const data = await response.json();
  return {
    statusCode: 200,
    body: JSON.stringify({ success: true, data })
  };
};
